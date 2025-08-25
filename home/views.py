{% load static %}
<!DOCTYPE html>
<html lang="end">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <title>{% block title %}Restaurant Management System{% endblock %}</title>

        <link href="https://fonts.googleapis.com/css2?family=segoe_UI:wght@300;400;600&display=swap" rel="stylesheet">

        <link rel="stylesheet" href="{% static 'css/static.css' %}">
        <link rel="icon" type="image/png" href="{% static 'images/favicon.png' %}"></head>
        <body>
            <header class="header">
            
                <div class="container">
                    <div class="logo-container">
                        <a href="{% url 'home:index' %}">
                            <img src="{% static 'images/restaurant-logo.png' %}" alt="Restaurant Management Logo" class="logo">
                        </a>
                    </div>
                    <nav class="navigation">
                        <ul>
                            <li><a href="{% url 'home:index' %}">Home</a></li>
                            <li><a href="{% url 'products:list' %}">Menu</a></li>
                            <li><a href="{%  url 'orders:list' %}">Orders</a></li>
                            <li><a href="{% url 'accounts:list' %}">Account</a></li>
                        </ul>
                    </nav>
                </div>
            </header>
            <main>
                {% block content %}
                {% endblock %}
            </main>
            <footer class="footer">
                <div class="footer-content">
                    <div class="footer-main">
                        <div class="footer-section">
                            <h3>Restaurant Management</h3>
                            <p>Your complete solution for restaurant operations, from order managment to inventory tracking.</p>
                            <div class="social-icons">
                                <a href="#" title="Facebook"><i class="fab fa-facebook-f"></i></a>
                                <a href="#" title="Twitter"><i class="fab fa-twitter"></i></a>
                                <a href="#" title="Instagram"><i class="fab fa-instagram"></i></a>
                                <a href="#" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                            </div>
                        </div>
                        <div class="footer-section">
                            <h3>Quick Links</h3>
                            <ul>
                                <li><a href="{% url 'home:index' %}">Home</a></li>
                                <li><a href="{% url 'products:list' %}">Menu</a></li>
                                <li><a href="{% url 'orders:list' %}">Orders</a></li>
                                <li><a href="{% url 'account:profile' %}">Account</a></li>
                            </ul></div>
                            <div class="footer-section">
                                <h3>Support</h3>
                                <ul>
                                    <li><a href="#help">Help Center</a></li>
                                    <li><a href="#contact">Contact Us</a></li>
                                    <li><a href="#faq">FAQ</a></li>
                                    <li><a href="#support">Technical Support</a></li>
                                </ul>
                            </div>
                            <div class="footer-section">
                                <h3>Contact Info</h3>
                                <p><i class="fas fa-phone"></i>+91 87945 25451</p>
                                <p><i class="fas fa-envelope"></i>info@restaurant.com</p>
                                <p><i class="fas fa-map-marker-alt"></i>123 Restaurant St, City, State 12345</p>
                            </div>
                    </div>
                    <div class="footer-bottom">
                        <div class="copyright">
                            <p>&copy; {% now "Y" %} Restaurant Management System. All rights reserved.</p>
                        </div>
                        <div class="footer-links">
                            <a href="#privacy">Privacy Policy</a>
                            <a href="#terms">Terms of Service</a>
                            <a href="#cookies">Cookie Policy</a>
                        </div>
                    </div>
                </div>
            </footer>
            <div>
                <footer class="footer">
                    <div class="footer-content">
                        <div class="opening-hours" style="margin-top:20px; font-weight:bold;color:#fff;">
                            <p>Opening Hours: Mon-Fri: 11am - 9pm | Sat-Sun:10am - 10pm</p>
                        </div>
                    </div>
                </footer>
            </div>

            <script>
                // Updated copyright year dynamically
                document.addEventListener('DOMContentLoad',function(){
                const currentYear = new Date().getFullYear();
                const copyrightElements = document.querySelectorAll('.copyright p');
                copyrightElements.forEach(function(element){
                element.innerHTML = element.innerHTML.replace(/\d{4}/,currentYear);
                });
                });
                </script>
        </body>
</html>

