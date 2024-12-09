# slai-web-projects

These are variants of websites developed by self-learning artificial intelligence (SLAI) based on a predefined specification. The specification is discussed with the user in advance to clarify project details. According to the requirements, creating a database, setting up a virtual environment, and configuring the settings for running the website on the server (e.g., Gunicorn, uWSGI) are not required. The primary goal of the testing was to evaluate SLAI's ability to implement a project with numerous editable files and executable terminal commands.

Although all three examples of websites were developed by SLAI based on the same technical specification, the websites differ from each other in appearance and the textual content on the homepage. There is an explanation for this difference: tasks are generated based on the context of the technical specification discussion. The tone for completing the technical specification is set by the user. The technical specification does not strictly define how the homepage of the website should look. The user did not provide explicit instructions on how the homepage should appear. For this reason, SLAI demonstrated a creative approach.
# technical specifications for development

### Technical Specification: Creating a Simple Django Website

#### Project Description
The task is to create a simple website with a single homepage using Django 4, which will display the site name "SLAI," a text description, an image, and the current date and time in a specified format. The site administrator should be able to edit the homepage content through the admin panel.

#### Key Requirements
1. **Homepage** (`127.0.0.1:8000`):
   - Display the heading "SLAI" centered on the page.
   - Below the heading, display a short description of the site.
   - Place an image below the description with a display size of 640x360 pixels.
   - Below the image, display the current date and time using JavaScript, formatted as `December 31, 15:15:15`.
   - All elements should be centered horizontally.

2. **Functionality**:
   - The current date and time should update every second using JavaScript.
   - The following fields should be editable through the admin panel:
     - Page heading (default empty).
     - Site description (default empty).
     - Image for the homepage (default empty).
   - Test data will be added to check functionality (e.g., heading, description, and image); after testing, this data should be removed to leave the page empty for the administrator to fill in.
   - A program should be created to test whether all requirements are met. If testing is successful, the task is complete; otherwise, any errors must be corrected.

3. **Admin Panel**:
   - The user should create an admin account manually. Instructions for creating this account will be provided in the project documentation. The credentials for the account should be:
     - Username: `admin`
     - Password: `admin2024`
     - Email: `scisoftdev@gmail.com`
   - Only three fields (heading, description, and image) should be visible and editable in the admin panel.

4. **Image**:
   - A single image will be displayed on the homepage, which the administrator can replace through the admin panel.
   - The image should automatically scale to 640x360 pixels when displayed on the website.
   - For testing purposes, use the test image located at `/home/scisoftdev/Pictures/Serenity_windows_xp.jpg`.

5. **Technologies to Use**:
   - The root project folder is located at `/home/scisoftdev/PycharmProjects/slai/Project`.
   - **Django 4** for the main code and admin panel.
   - **PostgreSQL** for the database, with the following connection parameters:
     - User: `postgres`
     - Password: `postgres`
     - Host: `127.0.0.1`
     - Port: standard PostgreSQL `5432`
     - Database: `slai_db` (the database already exists and is ready for use; no additional setup is required).
   - **Bootstrap 4** for page layout, included via CDN in the template.
   - **JavaScript** to display and update the current date and time.
   - You need to install all the necessary libraries.

6. **Additional Details**:
   - All test data (heading, description, and test image) should be removed from the database after successful testing so that the administrator can populate them independently.
   - The `<title>` tag of the page should be set to "SLAI" in the template to match the main heading on the homepage.
   - You need to install all the necessary libraries.

7. **Restrictions**:
   - There is no need to create a virtual environment.
   - The server should not be started during development (do not use the `python manage.py runserver` command).

#### Homepage Layout Structure
1. **Heading**: "SLAI" (centered).
2. **Text Description**: content from the admin panel (centered).
3. **Image**: positioned below the description, with a maximum size of 640x360 pixels (centered).
4. **Date and Time**: below the image, updating every second (centered).

#### Example Date and Time Format
- Format: `"December 31, 15:15:15"`
- The date and time should update every second for accurate display.

# review of results (after user edited content text)

## Project 1

![Image](https://github.com/scisoftdev/slai-web-projects/blob/main/images/Project_1.png)

## Project 2

![Image](https://github.com/scisoftdev/slai-web-projects/blob/main/images/Project_2.png)

## Project 3

![Image](https://github.com/scisoftdev/slai-web-projects/blob/main/images/Project_3.png)

## Admin Panel

![Image](https://github.com/scisoftdev/slai-web-projects/blob/main/images/Admin_panel.png)

