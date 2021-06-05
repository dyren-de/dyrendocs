# Dockerfile
FROM php:8.0-apache

LABEL maintainer="max@oppermann.fun"

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
