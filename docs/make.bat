@ECHO OFF

REM Save the current directory and change to the script's directory
pushd %~dp0

REM Command file for Sphinx documentation

REM Set the SPHINXBUILD variable if it is not already set
if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)

REM Define the source and build directories
set SOURCEDIR=source
set BUILDDIR=build

REM Check if sphinx-build is available
%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

REM If no argument is provided, show help
if "%1" == "" goto help

REM Handle the linkcheck target
if "%1" == "linkcheck" (
    %SPHINXBUILD% -b linkcheck %SOURCEDIR% %BUILDDIR%/linkcheck %SPHINXOPTS% %O%
    goto end
)

REM Run the specified target
%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end

REM Return to the original directory
popd
