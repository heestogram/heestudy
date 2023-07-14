from Kukipedia import Kukipedia

if __name__ == '__main__':
  #kuki = Kukipedia(target_title = "고려대학교")
  #print(kuki.wiki_summary_outline('ainize'))

  kuki = Kukipedia(target_title = "고려대학교")
  print(kuki.wiki_summary_section('ainize'))
