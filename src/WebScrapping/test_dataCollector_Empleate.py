import dataCollector_Empleate as dataCollector
import os

def test_get_configured_driver():
    '''Test the function get_configured_driver.'''
    driver = dataCollector.get_configured_driver()
    assert driver is not None
    driver.quit()

def browser_empleate():
    '''Test the function get_data_from_Jooble.'''
    folder = 'pdf_Files'
    previous_files = os.listdir(folder)

    driver = dataCollector.get_configured_driver()
    dataCollector.browser_empleate(driver)

    posterior_files = os.listdir(folder)
    assert previous_files is not posterior_files
    driver.quit()