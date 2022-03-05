import { mount } from '@vue/test-utils'
import HeadBar from '@/components/HeadBar.vue'

describe('HeadBar.vue', () => {
  it('renders HeadBar when passed', () => {
    const wrapper = mount(HeadBar)
    console.log(wrapper.contains('h1'))
  })
})
