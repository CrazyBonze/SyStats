import { m } from "mithril";
import { Header } from "./Header";

export class Layout {

        view(vnode) {
                return m('div', [
                        m(Header),
                        m('div', vnode.children)
                ])
        }
}
