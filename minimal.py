import flet


class MinimalFletClass:
    def __init__(self):
        self.__page = None

    def __call__(self, flet_page: flet.Page):
        self.__page = flet_page
        '''
        Create your app here
        '''
        self.__page.update()


if __name__ == '__main__':
    flet.app(target=MinimalFletClass())
