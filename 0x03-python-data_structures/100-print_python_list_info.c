#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	size_t size, i = 0;
	PyObject *obj;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zu\n", size);
	printf("[*] Allocated = %zu\n", ((PyListObject *)p)->allocated);
	for (; i < size; i++)
	{
		obj = PyList_GET_ITEM(p, i);
		printf("Element %zu: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
