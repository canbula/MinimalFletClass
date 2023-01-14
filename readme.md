# MinimalFletClass

A minimal class which generates a Flet application.

## Installation

It is just a boilerplate class, you can directly use it. However you need to install flet module first. You can use the package manager [pip] to install flet with one of these following commands.

```bash
pip install flet
pip3 install flet
python -m pip install flet
python3 -m pip install flet
py -m install flet
```

## Usage

As a first step you should import flet module.

```python
import flet
```

Then you can edit the name of the class and all the other information required to build your application.


```python
class MinimalFletClass:
    def __init__(self):
        self.__page = None

    def __call__(self, flet_page: flet.Page):
        self.__page = flet_page
        '''
        Create your app here
        '''
        self.__page.update()
```

At last you can check if your Python file is called directly or not. If it is, then you can create an instance of MinimalFletClass as:

```python
if __name__ == '__main__':
    flet.app(target=MinimalFletClass())
```

You can find these codes in minimal.py file. Also you can use boilerplate.py file as a more complete starting point for your first application.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)