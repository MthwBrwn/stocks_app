# Code 13: Model Relationships

Implement a new form for creating a Portfolio.
Implement the following UI features:

If a user navigates to /search and there are no Porftolio records available, provide feedback to the user and a link to /portfolio where a form is present to create a portfolio.

Upon adding a portfolio, redirect the user to /search.
If a user navigates to /portfolio and there are no Portfolio records available, provide feedback to the user and a form to create a portfolio.
Upon adding a portfolio, redirect the user to /search.

If one or more Portfolio records are available for the user, and they have submitted a search, the data returned to /company should now include a new drop down field (populated from the DB) with any available portfolios to select from.

Upon persisting a company to the DB, including a portfolio selection, redirect the user to /portfolio

If a user navigates to /portfolio and there are Portfolio and Company records available, provide a cleanly organized view that displays companies. Ensure that it’s easy to distinguish what portfolio each company belongs to.

Redeploy your application, and verify that you are able reach your deployed site. Manually check that all of your additional features are functioning correctly.

Note: Do not forget to run your migrations on EC2, and transition your new model relationships to the RDS instance.
