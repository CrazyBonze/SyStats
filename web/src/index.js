//import 'construct-ui/lib/index.css'
import "construct-ui/lib/index.css";
import { m } from "mithril";
import { Button } from "construct-ui";
import { SystemStats } from "./views/SystemStats";

const App = {
        view: () => {
                return m(Button,
                        {
                                label: "hello"
                        }
                )
        }
}

m.mount(document.body, App) //SystemStats)
