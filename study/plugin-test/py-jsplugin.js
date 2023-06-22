export default class HelloWorldPlugin {
    afterStartup(runtime) {
        const elem = document.createElement("h1");
        elem.innerText = "JSplugin1";
        document.body.appendChild(elem);
    }
}
