#!/bin/bash
mkdir -p ui_compiled
pyside6-uic ui/login.ui -o ui/login_ui.py
echo "UI compiled successfully!"