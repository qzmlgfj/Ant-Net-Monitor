import { mount } from '@vue/test-utils'
import HeadBar from '@/components/HeadBar.vue'
import { NH1, NButton } from 'naive-ui'

describe('HeadBar.vue', () => {
  it('renders HeadBar when passed', () => {
    const wrapper = mount(HeadBar)
    expect(wrapper.findComponent(NH1).text()).toBe('Ant Net Monitor')
    expect(wrapper.findComponent(NButton).text()).toBe('Change')
  })
})
