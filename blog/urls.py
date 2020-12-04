#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" blog """
from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]