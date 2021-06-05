# Dockerfile
FROM php:8.0-apache

LABEL maintainer="https://github.com/Max-42"

<<<<<<< HEAD
LABEL maintainer="max@oppermann.fun"
=======
MAINTAINER Max <max@oppermann.fun>
>>>>>>> 359d4e7f586f68269e19fac9d25c15e42a19f8dc

#Not important if you not using the same reverse proxy
ENV VIRTUAL_HOST=docs.dyren.de
ENV LETSENCRYPT_HOST=docs.dyren.de

COPY ./config/000-default.conf /etc/apache2/sites-available/000-default.conf

COPY ./config/apache2.conf  /etc/apache2/apache2.conf

RUN a2enmod rewrite

COPY ./src /var/www/
RUN chown -R www-data:www-data /var/www

EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
