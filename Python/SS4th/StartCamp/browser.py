import webbrowser

# webbrowser.open('https://www.google.com')
# webbrowser.open_new('https://www.naver.com')
# webbrowser.open_new_tab('https://www.daum.net')

heroes = ['iron man', 'batman', 'wonder woman', 'black widow']

for hero in heroes:
    print(hero)
    webbrowser.open('https://search.naver.com/search.naver?query=' + hero)