import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.randhawa.us/games/retailer/nyu.html")

html_source = driver.page_source

# Controls
restart_game = driver.find_element_by_id('practiceButton')
maintain = driver.find_element_by_id('maintainButton')
ten = driver.find_element_by_id('tenButton')
twenty = driver.find_element_by_id('twentyButton')
forty = driver.find_element_by_id('fortyButton')

click_count = 0


def main_game_click(click_type='maintain'):
    global click_count
    if click_count > 15:
        print('Error: cannot go over 15 weeks.')
        return
    if click_type == 'maintain':
        maintain.click()
    if click_type == 'ten':
        ten.click()
    if click_type == 'twenty':
        twenty.click()
    if click_type == 'forty':
        forty.click()
    click_count += 1


def get_results(results_df, performance_df, game_id):
    table = driver.find_elements_by_id("result-table")
    for row in table:
        for cell_number in range(1, 16):
            cell = row.find_elements_by_tag_name("tr")[cell_number]
            print(cell.text)
            results_list = cell.text.split(' ')
            print(results_list)
            results_df = results_df.append({'Round': game_id, 'Week': results_list[0], 'Price': results_list[1], 'Sales': results_list[2],
                               'Remaining': results_list[3]}, ignore_index=True)

    revenue = driver.find_element_by_id("rev")
    perfect = driver.find_element_by_id("perfect")
    difference = driver.find_element_by_id("percentage")
    print(f'Your revenue is: {revenue.text}')
    print(f'Perfect revenue is: {perfect.text}')
    print(f'Difference is: {difference.text}')
    performance_df = performance_df.append({'Round': game_id, 'Revenue': revenue.text, 'Perfect': perfect.text, 'Difference': difference.text.split(' ')[2]}, ignore_index=True)

    return results_df, performance_df

# Try out controls
'''
main_game_click()
main_game_click()
main_game_click()
main_game_click()
main_game_click('ten')
main_game_click()
main_game_click()
main_game_click()
main_game_click('twenty')
main_game_click()
main_game_click()
main_game_click()
main_game_click('forty')
'''

results_df = pd.DataFrame(columns=['Round', 'Week', 'Price', 'Sales', 'Remaining'])
performance_df = pd.DataFrame(columns=['Round', 'Revenue', 'Perfect', 'Difference'])

for i in range(1, 31):
    main_game_click()
    main_game_click()
    main_game_click()
    main_game_click()
    main_game_click('ten')
    main_game_click()
    main_game_click()
    main_game_click()
    main_game_click('twenty')
    main_game_click()
    main_game_click()
    main_game_click()
    main_game_click('forty')
    results_df, performance_df = get_results(results_df=results_df, performance_df=performance_df, game_id=i)
    restart_game.click()
    click_count = 0


results_df.to_csv('./data/game_results.csv')
performance_df.to_csv('./data/performance.csv')