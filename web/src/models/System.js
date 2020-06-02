// src/models/System.js
var m = require("mithril")

var System = {
        stats: null,
        loadSystem: function() {
                return m.request({
                        method: "GET",
                        url: "/api/stats/system",
                }).then(function(result) {
                        console.log(result);
                        System.stats = result;
                })
        },
}

module.exports = System
