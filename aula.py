from chrome_page import ChromePage
import pyautogui

# abrir navagador com pyautogui
chrome_page = ChromePage()
chrome_page.open_chrome()
# escrever no navegador
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")