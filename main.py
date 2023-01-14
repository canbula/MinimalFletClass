import flet


class MinimalFletClass:
    def __init__(self):
        self.__page = None
        self.__app_icon = flet.Icon(name=flet.icons.CHECK, size=48)
        self.__app_title = flet.Text(value="Minimal Flet Class", style=flet.TextThemeStyle.DISPLAY_SMALL)
        self.__theme_toggle_button = flet.IconButton(
            icon=flet.icons.SUNNY,
            tooltip="Toggle Theme",
            on_click=self.__toggle_theme
        )

    def __init_window(self):
        self.__page.title = "Minimal Flet Class"
        self.__page.window_min_width = 500
        self.__page.window_min_height = 500
        self.__page.window_width = 500
        self.__page.window_height = 500
        self.__page.window_frameless = False
        self.__page.window_always_on_top = True
        self.__page.window_focused = True
        self.__page.window_center()
        self.__page.theme_mode = flet.ThemeMode.LIGHT

    def __toggle_theme(self, _):
        if self.__page.theme_mode == flet.ThemeMode.LIGHT:
            self.__page.theme_mode = flet.ThemeMode.DARK
        else:
            self.__page.theme_mode = flet.ThemeMode.LIGHT
        self.__page.update()

    def __call__(self, flet_page: flet.Page):
        self.__page = flet_page
        self.__init_window()
        self.__page.add(
            flet.Row(
                wrap=False,
                alignment=flet.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    flet.Row(
                        wrap=False,
                        controls=[
                            self.__app_icon,
                            self.__app_title
                        ]
                    ),
                    self.__theme_toggle_button
                ]
            )
        )
        '''
        Create your app here
        '''
        self.__page.update()


if __name__ == '__main__':
    flet.app(target=MinimalFletClass())
