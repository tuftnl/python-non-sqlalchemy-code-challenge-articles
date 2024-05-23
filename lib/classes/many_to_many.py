class Article:

    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.add_article(self)
    
    def __repr__(self):
        return f"Article('{self.author}', '{self.magazine}', '{self.title}')"
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise Exception("Customer musst be an instance of the Customer class")
    
    @classmethod
    def add_article(cls, new_article):
        cls.all.append(new_article)

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise Exception("Customer musst be an instance of the Magazine class")
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, '_title'):
            self._title = title
        else:
            raise Exception("Name must be a string between 5 and 50 characters")



class Author:

    all = []

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Author('{self.name}')"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) and not hasattr(self, '_name'):
            self._name = name
        else:
            raise Exception("Name must be a string more than 0 characters") 

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magazine_set = {article.magazine for article in self.articles()}
        return list(magazine_set)

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        magazine_categories = {magazine.category for magazine in self.magazines()}
        if len(magazine_categories) > 0:
            return list(magazine_categories)
        else:
            return None



class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
    
    def __repr__(self):
        return f"Magazine('{self.name}', '{self.category}')"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception("Must be alphabetical characters between 2 and 16 in length.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and 0 < len(new_category):
            self._category = new_category
        else:
          raise Exception("Name must be a string more than 0 characters")

    @classmethod
    def add_new_magazine(cls, new_magazine):
        cls.all.append(new_magazine)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        author_set = {article.author for article in self.articles()}
        return list(author_set)

    def article_titles(self):
        titles_set = {article.title for article in self.articles()}
        if len(titles_set) > 0:
            return list(titles_set)
        else:
            return None

    def contributing_authors(self):
        list_of_authors = [article.author for article in self.articles()]
        contributing_authors = [author for author in self.contributors() if list_of_authors.count(author) > 2]
        if contributing_authors:
            return contributing_authors
        else:
            return None

    @classmethod
    def top_publisher(cls):
        is_articles = False
        for magazine in cls.all:
            if [article for article in Article.all if article.magazine == magazine]:
                is_articles = True
            if is_articles == True:
                top_publisher = max(cls.all, key=lambda magazine: len(magazine.articles()))
                return top_publisher
            else:
                return None