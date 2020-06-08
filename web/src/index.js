import { mount, route, m } from "mithril";
import "construct-ui/lib/index.css";
import { SystemStats } from "./views/SystemStats";
import { Home } from "./views/Home";
import { Settings } from "./views/Settings";
import { Layout } from "./views/Layout";

const routes = {
        "/home": {
                render: () => {
                        return m(Layout, m(Home))
                },
        },
        "/settings": {
                render: () => {
                        return m(Layout, m(Settings))
                },
        },
        "/systems": {
                render: () => {
                        return m(Layout, m(SystemStats))
                },
        },
};

route(document.body, "/home", routes)
