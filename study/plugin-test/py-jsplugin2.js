class PyHelloWorld extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `<ul><li>jsplugin2</li></ul>`;
        this.mount_name = this.id;
    }
}

export default class HelloWorldPlugin {
    afterStartup(runtime) {
        // Create a custom element called <py-hello-world>
        customElements.define("py-jsplugin", PyHelloWorld);

        // // Add the custom element to the page so we can see it
        // const elem = document.createElement("py-jsplugin");
        // document.body.append(elem);
    }
}
