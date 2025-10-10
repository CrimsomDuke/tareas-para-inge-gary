from django.shortcuts import render
from dependencies_manager import DependenciesManager

dependencies_manager = DependenciesManager.get_instance()

products_repository = dependencies_manager.product_repository

def index(request):

    query = request.GET.get('q', '')
    if(query):
        products = products_repository.search_products_by_name(query)
    else:
        products = products_repository.get_all_products()

    context = {
        'title': 'Tienda - Home',
        'message': 'Bienvenido a la tienda! Renderizando plantilla HTML desde Django.',
        'productos': products
    }
    return render(request, 'tienda/lista.html', context)

def product_detail(request, id):
    producto = products_repository.get_product_by_id(id)
    print(producto)  # Debugging: Print the product object to verify its contents
    context = {
        'title': f'Detalle de {producto.nombre}',
        'producto': producto
    }
    return render(request, 'tienda/detalle.html', context)