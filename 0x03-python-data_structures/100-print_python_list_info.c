#include <stdio.h>
#include <python3.8/Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer to a PyObject struct
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *obj;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
