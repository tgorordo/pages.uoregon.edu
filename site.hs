--------------------------------------------------------------------------------
{-# LANGUAGE OverloadedStrings #-}
import           Data.Monoid (mappend)
import           Hakyll

import Text.Pandoc.Extensions (Extension(..), enableExtension)
import Text.Pandoc.Options

import System.Process (readCreateProcess, shell, CreateProcess(..))
import System.FilePath (takeDirectory, takeFileName)

import Data.Maybe (fromMaybe)
import Control.Monad (filterM)

--------------------------------------------------------------------------------
main :: IO ()
main = hakyll $ do
    match "files/**" $ do
        route   idRoute
        compile copyFileCompiler

    match "css/*" $ do
        route   idRoute
        compile compressCssCompiler

    match (fromList []) $ do
        route   $ setExtension "html"
        compile $ pandocCompiler
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls

    -- Courses
    match "courses/uoph611_Th-Mechanics/*" $ do
        route idRoute
        compile copyFileCompiler

    match "courses/uoph410-510c_Sci-Comp/resources.md" $ do
        route $ setExtension "html"
        compile $ pandocCompiler
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls
    match "courses/uoph410-510c_Sci-Comp/*" $ do
        route idRoute
        compile copyFileCompiler

    match "courses/uoph410-510a_Image-Analysis/setup.md" $ do
        route $ setExtension "html"
        compile $ pandocCompiler
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls
    match (foldl1 (.||.) $
            fromGlob "courses/uoph410-510a_Image-Analysis/wk1/s0.py" :
            [ fromGlob ("courses/uoph410-510a_Image-Analysis/wk" ++ n ++ "/s" ++ n ++ ".py")
            | n <- map show [1..8] ]) $ do
        route $ setExtension "html"
        compile $ do
            fp <- toFilePath <$> getUnderlying
            let dir   = takeDirectory fp
                fnm   = takeFileName fp
                outfp = fnm ++ ".html"
                cmd = "cd " ++ dir ++ " && uv run marimo export html " ++ fnm ++ " --output " ++ outfp ++ " --force --no-sandbox"
            unsafeCompiler $ readCreateProcess (shell cmd) ""
            result <- unsafeCompiler $ readFile (dir ++ "/" ++ outfp)
            makeItem result
    match (foldl1 (.||.) 
            [ fromGlob ("courses/uoph410-510a_Image-Analysis/wk" ++ n ++ "/*")
            | n <- map show [1..8] ]) $ do
        route   idRoute
        compile copyFileCompiler

    match "courses/uoph444-544_Intro-BioPhysics/**" $ do
        route idRoute
        compile copyFileCompiler

    match "courses/uoph25X_Foundations/*" $ do
        route idRoute
        compile copyFileCompiler

    match "posts/*" $ do
        route $ setExtension "html"

        compile $ getResourceString
            >>= withItemBody (return . doubleBackslashes)
            >>= renderPandoc
            >>= loadAndApplyTemplate "templates/post.html" postCtx
            >>= loadAndApplyTemplate "templates/default.html" postCtx
            >>= relativizeUrls


    create ["archive.html"] $ do
        route idRoute
        compile $ do
            posts <- recentFirst =<< filterM (isPublished . itemIdentifier) =<< loadAll "posts/*"
            let archiveCtx =
                    listField "posts" postCtx (return posts) `mappend`
                    constField "title" "Archives"            `mappend`
                    defaultContext

            makeItem ""
                >>= loadAndApplyTemplate "templates/archive.html" archiveCtx
                >>= loadAndApplyTemplate "templates/default.html" archiveCtx
                >>= relativizeUrls


    match "README.md" $ do
        route $ constRoute "index.html"
        compile $ do
            posts <- recentFirst =<< filterM (isPublished . itemIdentifier) =<< loadAll "posts/*"
            let indexCtx =
                    listField "posts" postCtx (return posts) `mappend`
                    defaultContext

            getResourceString
                >>= withItemBody (return . doubleBackslashes)
                >>= renderPandoc
                >>= applyAsTemplate indexCtx
                >>= loadAndApplyTemplate "templates/default.html" indexCtx
                >>= relativizeUrls

    match "templates/*" $ compile templateBodyCompiler

--------------------------------------------------------------------------------
postCtx :: Context String
postCtx =
    dateField "date" "%B %e, %Y" `mappend`
    defaultContext

doubleBackslashes :: String -> String
doubleBackslashes = concatMap (\c -> if c == '\\' then "\\\\" else [c])

isPublished :: MonadMetadata m => Identifier -> m Bool
isPublished ident = do
    val <- getMetadataField ident "published"
    return $ fromMaybe False $ fmap (== "true") val


