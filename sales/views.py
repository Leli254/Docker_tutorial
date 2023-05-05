#external imports
from io import BytesIO
import base64
import pandas as pd
import matplotlib.pyplot as plt

#django imports
from django.shortcuts import render
from django.views.generic import TemplateView

#local imports
from .models import SalesData


#views
def sales_data_view(request):
    # Retrieve the sales data from the database
    sales_data = SalesData.objects.all()

    # Convert the sales data to a Pandas DataFrame
    sales_df = pd.DataFrame(list(sales_data.values()))

    # Calculate the total sales by month
    sales_by_month = sales_df.groupby('month')['sales'].sum()

    # Create a bar chart of the sales by month
    plt.bar(sales_by_month.index, sales_by_month.values)
    plt.title('Total Sales by Month')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Convert the plot to a base64-encoded string to display in the template
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    # Pass the sales data and chart data to the template
    context = {'sales_chart': image_base64, 'salesdata': sales_data}
    return render(request, 'sales/sales_chart.html', context)


#Above view as class based view
class SalesDataView(TemplateView):
    template_name = 'sales/sales_chart.html'

    def get_context_data(self, **kwargs):
        # Retrieve the sales data from the database
        sales_data = SalesData.objects.all()

        # Convert the sales data to a Pandas DataFrame
        sales_df = pd.DataFrame(list(sales_data.values()))

        # Calculate the total sales by month
        sales_by_month = sales_df.groupby('month')['sales'].sum()

        # Create a bar chart of the sales by month
        plt.bar(sales_by_month.index, sales_by_month.values)
        plt.title('Total Sales by Month')
        plt.xlabel('Month')
        plt.ylabel('Sales')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Convert the plot to a base64-encoded string to display in the template
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        buffer.close()

        # Return the chart data to the template
        return {'sales_chart': image_base64}