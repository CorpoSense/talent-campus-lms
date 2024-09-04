import { describe, expect, it } from "vitest"
import { mount, shallowMount } from '@vue/test-utils'
import Home from '@/views/Home.vue'
import About from '@/views/About.vue'

const app = {
    name: "TalentCampus",
    version: "0.0.1"
}

describe('Run App', () => {

    it('check app params', () => {
        expect(app.name).toBe("TalentCampus")
    })

    it('make sure the app is running', () => {
        expect(1).toBe(1)
    })

    it('Show home view', () => {
        expect(Home).toBeTruthy();
        const wrapper = shallowMount(Home);
        expect(wrapper.text()).toContain('Courses');
    })

    it('make sure the about page exists', async () => {
        const wrapper = mount(About)
        expect(wrapper.text()).toContain('About')
        await wrapper.get('.btn-contact').trigger('click')
    })

})
