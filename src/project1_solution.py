def keyword_search(list, keyword):
  for item in list:
    if type(item) == float:
      print("This item is float value")
    if type(item) == str:
      print("This item is string value")
      if (item==keyword):
        print("We found the keyword")
    if type(item) == int:
      print("This item is integer value")
    

keyword_search([5,6,7,8,9 ,"string", "string_1"], "string_1")