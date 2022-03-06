import { mount } from '@vue/test-utils'
import { createRouter, createWebHistory } from 'vue-router'
import { NSpace, NH1, NButton } from 'naive-ui'

import { routes } from '@/router'
import store from '@/utils/store'

import HeadBar from '@/components/HeadBar.vue'
import SideBar from '@/components/SideBar.vue'

describe('HeadBar.vue', () => {
    test('renders HeadBar when passed', async () => {
        const wrapper = mount(HeadBar)
        expect(wrapper.findComponent(NSpace).exists()).toBe(true)
        expect(wrapper.findComponent(NH1).text()).toBe('Ant Net Monitor')
        expect(wrapper.findComponent(NButton).text()).toBe('Change')

        wrapper.findComponent(NButton).trigger('click')
        expect(wrapper.emitted().hasOwnProperty('changeTheme')).toBe(true)
    })
})

let router;

beforeEach(async () => {
    router = createRouter({
        history: createWebHistory(),
        routes: routes,
    })

    router.push('/')
    await router.isReady()
});

describe('SideBar.vue', () => {
    test('renders SideBar when passed', async () => {
        const wrapper = mount(SideBar, {
            global: {
                plugins: [router]
            }
        })

        console.log(wrapper.find('#sidebar .n-menu-item a').attributes('href'))
    })
})


