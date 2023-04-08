import pytest
import os
from selene import be, have, browser, command


def test_submit_form(browser_setting):
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('Ivan')
    browser.element('#lastName').should(be.blank).type('Ivanov')
    browser.element('#userEmail').should(be.blank).type('test@test.ru')
    browser.element('[name=gender][value=Male] + label').click()
    browser.element('#userNumber').should(be.blank).type('89001000000')

    browser.execute_script("window.scrollBy(0, 500)")

    browser.element('#dateOfBirthInput').should(be.clickable).click()
    browser.element('.react-datepicker__month-select').should(be.clickable).click()
    browser.element('[value="11"]').should(be.clickable).click()
    browser.element('.react-datepicker__year-select').should(be.clickable).click()
    browser.element('[value="1900"]').should(be.clickable).click()

    browser.element('div[class="react-datepicker__day react-datepicker__day--018"]').should(be.clickable).click()
    browser.element('#subjectsInput').should(be.blank).type('eng').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/images.jpg')
    browser.element("#currentAddress").should(be.blank).type('SaintP')

    browser.element('#fixedban').perform(command.js.remove)

    browser.element('#react-select-3-input').should(be.blank).type('NCR').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Delhi').press_enter().press_enter()

    browser.element('//tbody/tr[1]/td[2]').should(have.text('Ivan Ivanov'))
    browser.element('//tbody/tr[2]/td[2]').should(have.text('test@test.ru'))
    browser.element('//tbody/tr[3]/td[2]').should(have.text('Male'))
    browser.element('//tbody/tr[4]/td[2]').should(have.text('8900100000'))
    browser.element('//tbody/tr[5]/td[2]').should(have.text('18 December,1900'))
    browser.element('//tbody/tr[6]/td[2]').should(have.text('English'))
    browser.element('//tbody/tr[7]/td[2]').should(have.text('Reading'))
    browser.element('//tbody/tr[8]/td[2]').should(have.text('images.jpg'))
    browser.element('//tbody/tr[9]/td[2]').should(have.text('SaintP'))
    browser.element('//tbody/tr[10]/td[2]').should(have.text('NCR Delhi'))