// src/views/SystemStats.js
import { m } from "mithril";
import { Table } from 'construct-ui';
import { System } from "../models/System";

export class SystemStats {

        constructor() {
                this.system = new System();
                this.stats = {};
        }


        oninit() {
                this.system.loadSystem().then((result) => {
                        this.stats = result;
                });
        }

        view() {
                return [
                        m(Table, {id: ".system-stats"},
                        [
                                m("tr", {}, [
                                        m("th", 'System ID'),
                                        m("td", this.stats['system_id']),
                                ]),
                                m("tr", {}, [
                                        m("th", 'Uptime'),
                                        m("td", this.stats['uptime']),
                                ]),
                                m("tr", {}, [
                                        m("th", 'Boot Time'),
                                        m("td", this.stats['boottime']),
                                ]),
                                m("tr", {}, [
                                        m("th", 'System'),
                                        m("td", this.stats['system']),
                                ]),
                                m("tr", {}, [
                                        m("th", 'Node'),
                                        m("td", this.stats['node']),
                                ]),
                                m("tr", {}, [
                                        m("th", 'Release'),
                                        m("td", this.stats['release']),
                                ]),
                                m("tr", {}, [
                                        m("th", 'Version'),
                                        m("td", this.stats['version']),
                                ]),
                                m("tr", {}, [
                                        m("th", 'Machine'),
                                        m("td", this.stats['machine']),
                                ]),
                                m("tr", {}, [
                                        m("th", 'Processor'),
                                        m("td", this.stats['processor']),
                                ])
                        ]
                )
                ]
        }
}
