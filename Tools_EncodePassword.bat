@ECHO OFF

cd %~dp0

python -c "import Tools; Tools.encode_password()"

PAUSE