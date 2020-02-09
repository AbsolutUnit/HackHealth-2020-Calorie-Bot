from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import argparse
'''
parser = argparse.ArgumentParser()
parser.add_argument("calories",help="How many calories?")
parser.add_argument("meals",help="How many meals?")
args = parser.parse_args()
cals = args.calories
meal_num = args.meals
'''    
     
class Plan:
    def __init__(self,cal=2000,meal=3):
        self.CALORIES = int(cal)
        self.MEALS_NUM = int(meal)
        if self.MEALS_NUM > 9:
            self.MEALS_NUM=9
        if self.MEALS_NUM < 1:
            self.MEALS_NUM = 1
        self.SRC = 'https://www.eatthismuch.com/'
        self.meal_list = []
        self.calories = []

    def makePlan(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('chromedriver --log-level=OFF')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-logging")
        options.add_argument('log-level=3')
        
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

        driver.get(self.SRC)

        time.sleep(0.5)

        driver.find_element_by_id('cal_input').send_keys(self.CALORIES)

        meal = Select(driver.find_element_by_id('num_meals_selector'))

        meal.select_by_visible_text(str(self.MEALS_NUM)+' meals')
        #print(str(self.MEALS_NUM)+' meals')
        driver.find_element_by_class_name('btn.btn-lg.btn-block.btn-orange.gen_button').click()

        time.sleep(5)
        
        titles = driver.find_elements_by_class_name('col.text-dark-gray.text-large.text-strong.print_meal_title.wrap_or_truncate.pr-0')
  
        
        meals = driver.find_elements_by_class_name('meal_box.meal_container.row')
       # meal_num = 0
        for meal in meals:
            #title = meal.find_element_by_class_name('col.text-dark-gray.text-large.text-strong.print_meal_title.wrap_or_truncate.pr-0')
            totCal = meal.find_element_by_class_name('cal_amount.text-small.text-light-gray')
            
            #print(title.text)
            if (totCal.text == ""):
                continue
            
            foods = meal.find_elements_by_class_name('diet_draggable.ui-sortable-handle')
            food_list = []
            for food in foods:
                
                img = food.find_element_by_class_name('food_image')
                link = img.get_attribute('style')
                #Find the first open quote and chop there
                link = link[link.index('\"')+1:]
                #Find the next quote and chop off the end
                link = link[:link.index('\"')]
                #print(link)
                name = food.find_element_by_class_name('print_name')
                amt = food.find_element_by_class_name('amount_input').get_attribute("value")
                serv = food.find_element_by_class_name('food_units_selector')
                
                serv_name = serv.find_elements_by_tag_name('option')[1]
            
                #print (name.text + " - " + amt + " " + serv_name.text)
                food_list.append([str(name.text),str(amt +" " + serv_name.text),str(link)])
            #print('Total Calories :'+totCal.text + "\n")
            #self.meal_list[meal_num] = food_list
            self.meal_list.append(food_list)
            self.calories.append(str(totCal.text))
            #self.calories[meal_num] = str(totCal.text)
            #meal_num += 1
        driver.quit()
        print(len(self.meal_list))
        print(self.meal_list)
        print(self.meal_list[0])
        print(self.calories)
        '''
        with open('meals.txt','w') as json_file:
            json.dump(self.meal_list,json_file)
        with open('calories.txt','w') as json_file:
            json.dump(self.calories,json_file)
        '''
'''
x = Plan(cals,meal_num)
x.makePlan()
'''