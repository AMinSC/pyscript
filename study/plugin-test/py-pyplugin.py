from pyscript import Plugin
from pyscript import js

plugin = Plugin("PyHelloWorld")

@plugin.register_custom_element("py-pyplugin")
class PyHelloWorld2:
    def __init__(self, element):
        self.element = element

    def connect(self):
        self.element.innerHTML = "<div>python plugin</div>"
        one = js.document.querySelector("py-script")
        two = one.innerText.replace("$", "js.document.querySelector")
        js.console.log(one.innerHTML, two)
        one.innerHTML = two
