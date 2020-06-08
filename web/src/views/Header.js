import { m, Link, route } from "mithril";
import { ControlGroup, Button, Input, Icon, Icons, Select, Spinner, CustomSelect } from "construct-ui";
import { Col, Grid } from "construct-ui";
import { Tabs, TabItem, Size, Switch, Align } from "construct-ui";

const routes = [
        {
                route: '/home',
                label: 'Home',
        },
        {
                route: '/systems',
                label: 'Systems',
        },
        {
                route: '/settings',
                label: 'Settings',
        }
]

export class Header {

        oninit(vnode) {
                this.active = route.get();
        }

        view(vnode) {
                return m('div', [
                        m(Tabs, {bordered: true, align: 'left', size: 'lg'},
                                [
                                        routes.map(item => m(TabItem, {
                                                label: [
                                                        item.label === 'Settings' && m(Icon, {
                                                                name: Icons.SETTINGS,
                                                                style: 'margin-right: 5px'
                                                        }),
                                                        item.label
                                                ],
                                                active: this.active === item.route,
                                                onclick: () => {
                                                        route.set(item.route);
                                                        this.active = item.route;
                                                },
                                        }))
                                ]),
                ])
        }
}


