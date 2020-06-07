// src/models/System.js
import { request } from "mithril";

export class System {

        loadSystem() {
                return request({
                        method: "GET",
                        url: "/api/stats/system",
                }).then((result) => {
                        return result;
                });
        }
}
