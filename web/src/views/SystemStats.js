// src/views/SystemStats.js
import { m } from "mithril";
import { System } from "../models/System";

module.exports = {
        oninit: System.loadSystem,
        view: function() {
                return m("ul", {id: ".system-stats"}, [
                        m("li", 'hello'),//System.stats['system_id'])
                        m("li", 'world')//System.stats['system_id'])
                        ]
                )
        },
}
