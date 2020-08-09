import time
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import download_songs


def find_playlist(input_text):

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://open.spotify.com/search/' + input_text)

    timeout = 5
    try:
        element_present = EC.presence_of_element_located(
            (By.XPATH, '//*[@id="searchPage"]/div/div/section[5]/div/div[2]/div/div/div[4]'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        time.sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="searchPage"]/div/div/section[5]/div/div[2]/div/div/div[4]').click()

    try:
        element_present = EC.presence_of_element_located(
            (By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div[2]/section/div[1]/div[5]/span/h1'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        time.sleep(1)
        # Finding playlist name
        try:
            playlist_name = driver.find_element_by_xpath(
                '//*[@id="main"]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div[2]/section/div[1]/div[5]/span/h1').text
        except:
            playlist_name = "--missing--"
        # Finding playlist description
        try:
            playlist_description = driver.find_element_by_xpath(
                '//*[@id="main"]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div[2]/section/div[1]/div[5]/h2[2]/p/span').text
        except:
            playlist_description = "--missing--"

        # Finding playlist likes
        try:
            playlist_likes = driver.find_element_by_xpath(
                '//*[@id="main"]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div[2]/section/div[1]/div[5]/div/span[1]').text
        except:
            playlist_likes = "--missing--"

        # Finding playlist duration
        try:
            playlist_duration = driver.find_element_by_xpath(
                '//*[@id="main"]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div[2]/section/div[1]/div[5]/div/span[2]').text
        except:
            playlist_duration = "--missing--"

        playlist = driver.find_elements_by_class_name('tracklist-row')

        songs_name = []
        songs_path = []

        # for test purpose downloading only two songs

        for p in playlist[:2]:

            name = p.find_element_by_class_name('tracklist-name').text
            meta_data = (p.find_element_by_class_name(
                'second-line').text).replace('\n', ' ').replace(' • ', '')

            name_list = ('Official song' + str(name) + str(meta_data))
            songs_name.append(name)
            # print(meta_data)
            songs_path.append(download_songs.main(name_list))
            # print('____________________________________________________________________________________________________________________________________')

    print('___________________________________________________________________________________________________________________________________________')
    for i in range(len(songs_name)):
        print(songs_name[i])
        print(songs_path[i])
        print('___________________________________________________________________________________________________________________________________________')

    print("Playlist Name : " + playlist_name)
    print("Playlist Description : " + playlist_description)
    print("Playlist Likes : " + playlist_likes)
    print("Playlist Duration : " + playlist_duration)

    driver.close()


if __name__ == "__main__":
    find_playlist(sys.argv[1])
