describe('Test the frontend part', () => {
    beforeEach(() => {
        if (Cypress.env('mode') === 'develop')
            cy.visit('http://127.0.0.1:8080/')
        else if (Cypress.env('mode') === 'e2e')
            cy.visit('http://127.0.0.1:5000/')
    })

    it('renders head bar and changes theme correctly', () => {
        cy.get('#header .n-h1').contains('Ant Net Monitor')

        // White at first time
        cy.get('#container').should('have.css', 'background-color', 'rgb(255, 255, 255)')

        //Change to black
        cy.get('#change-theme').click()
        cy.get('#container').should('have.css', 'background-color', 'rgb(16, 16, 20)')

        //Change to white
        cy.get('#change-theme').click()
        cy.get('#container').should('have.css', 'background-color', 'rgb(255, 255, 255)')
    })

    it('renders info component when munu item clicked', () => {
        cy.get('.n-menu-item a').each((el) => {
            //cy.wrap(el).click()
            cy.visit(el.prop('href'))
            cy.get('#info .n-h1').contains(el.text())
        })
    })

    it('renders dashboard component correctly', () => {
        cy.get('#swap-status').should('exist')
        cy.get('#cpu-status').should('exist')
        cy.get('#ram-status').should('exist')
    })
})
