from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver = webdriver.Chrome()

try:
    driver.get("https://app.sportclub.com")
    time.sleep(3)

    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Hacerse socio')]")
    btn.click()
    time.sleep(2)

    assert "Formulario" in driver.page_source or "Datos" in driver.page_source

    tracking_data = {
        "event": "hacerse_socio_click",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "device": "QA-Selenium"
    }

    response = requests.post("https://mi-api.com/track", json=tracking_data)
    print(f"Evento enviado: {response.status_code}")

finally:
    driver.quit()