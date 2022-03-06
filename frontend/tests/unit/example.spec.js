import { mount } from '@vue/test-utils'
import HeadBar from '@/components/HeadBar.vue'
import SideBar from '@/components/SideBar.vue'
import { routes } from '@/router'
import { createRouter, createWebHistory } from 'vue-router'
import { NSpace,NH1, NButton } from 'naive-ui'

describe('HeadBar.vue', () => {
    it('renders HeadBar when passed', () => {
        const wrapper = mount(HeadBar)
        expect(wrapper.findComponent(NSpace).exists()).toBe(true)
        expect(wrapper.findComponent(NH1).text()).toBe('Ant Net Monitor')
        expect(wrapper.findComponent(NButton).text()).toBe('Change')
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

test('SideBar.vue', async () => {
    const wrapper = mount(SideBar, {
        global: {
            plugins: [router]
        }
    })

    console.log(wrapper.find('#sidebar .n-menu-item a').attributes('href'))
})