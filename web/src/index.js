import { mount, route, m } from "mithril";
import "construct-ui/lib/index.css";
import { SystemStats } from "./views/SystemStats";

const routes = {
        "/": {
                render: () => {
                        return m(SystemStats)
                }
        },
};

//mount(document.body, SystemStats)
route(document.body, "/", routes)
