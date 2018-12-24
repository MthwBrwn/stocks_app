# Lab 12: Templating

##Features

- [x] Utilizing template inheritance within your application, ensure that each of your views is built from a template partial which inherits from the base.html, with at least one content block abstraction.

- [x] Take advantage of url_for to generate your urls rather than manually managing them.
Update your search.html to include the use of the form object passed as context data.
This page will include the use of a form for accepting a stock symbol and utilizing that data for the search.

- [x] You will also need a csrf_token included in your forms.

- [x] Implement a company.html template which will provide the user with a preview of the company information. If the user chooses to persist that data in the database, a form capture will occur which will POST the data to the database and then redirect the user to their Portfolio detail view.

- [x] This page will also include a hidden form, which will require the implementation of a new form class.

- [x] Update the portfolio.html document to render context from the database. This context should include, at least, the companies that the user has persisted.
Ensure that your templates are taking advantage of conditional logic and flow control for rendering context in the right place, at the right time.

- [x] Take advantage of template filters to control the data presentation layer without the need of additional styles. For example, data from your persistence layer may be all lowercase; capitalize the first letter of that data or uppercase the whole of the text in the case of acronyms.

- [x] Capture occurrences of errors within your application (i.e. the user adds the same record two or more times), and flash a message to the client view; you may need to determine whether a flashed message is appropriate rather than a redirect to a 404 page.

- [x] Redeploy your application, and verify that you are able reach your deployed site. Manually check that all of your additional features are functioning correctly.
Testing

- [x] You are required to meet or exceed an 80% coverage benchmark for this application.



