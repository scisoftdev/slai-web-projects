import os

# Путь к файлу шаблона home.html
template_file_path = '/home/scisoftdev/PycharmProjects/slai/Project/slai/templates/slai/home.html'

# HTML содержимое для home.html
new_template_content = """
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;{{ content.title }}&lt;/title&gt;
    &lt;style&gt;
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            font-family: Arial, sans-serif;
        }
        img {
            max-width: calc(1920px / 3);
            max-height: calc(1080px / 3);
            object-fit: cover;
            margin: 20px 0;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        #time {
            font-size: 24px;
            margin-top: 20px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;{{ content.title }}&lt;/h1&gt;
    &lt;p&gt;{{ content.text }}&lt;/p&gt;

    {% if content.image %}
    &lt;img src="{{ content.image.url }}" alt="Main Image"&gt;
    {% endif %}

    &lt;div id="time"&gt;&lt;/div&gt;

    &lt;script&gt;
        function updateTime() {
            const timeElement = document.getElementById('time');
            const now = new Date();
            timeElement.textContent = 'Текущее время: ' + now.toLocaleTimeString();
        }

        setInterval(updateTime, 1000);
        updateTime();
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
"""

# Убедиться, что все директории для шаблонов созданы
os.makedirs(os.path.dirname(template_file_path), exist_ok=True)

# Записать новое содержимое в файл home.html
try:
    with open(template_file_path, 'w') as file:
        file.write(new_template_content.strip())
    print(f"Файл {template_file_path} успешно обновлен.")
except Exception as e:
    print(f"Ошибка при обновлении файла: {e}")
