# bokeh_plot.py
from bokeh.io import output_notebook
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Button, TextInput, CustomJS, Div, Select
from bokeh.plotting import figure
import numpy as np
from scipy.stats import norm, lognorm, expon

def create_bokeh_normal_plot():
    # Initialize notebook display for Bokeh
    output_notebook()

    # Create input widgets for mu and sigma
    plain_text_div = Div(text="Distribution 1")
    mu_input = TextInput(value='0', title='Mu:', width=70)
    sigma_input = TextInput(value='1', title='Sigma:', width=70)
    plain_text_div_2 = Div(text="Distribution 2")
    mu_input_2 = TextInput(value='0', title='Mu:', width=70)
    sigma_input_2 = TextInput(value='1', title='Sigma:', width=70)

    # Create a plot
    p = figure(title='Density', x_axis_label='x', y_axis_label='Density', height=300)
    source = ColumnDataSource(data={'x': [], 'y': []})
    p.line('x', 'y', source=source, line_width=2, line_color='red')
    source2 = ColumnDataSource(data={'x': [], 'y': []})
    p.line('x', 'y', source=source2, line_width=2, line_color='blue')

    p_cum = figure(title='Cumulative', x_axis_label='x', y_axis_label='Cumulative', height=300)
    source_cum = ColumnDataSource(data={'x': [], 'y': []})
    p_cum.line('x', 'y', source=source_cum, line_width=2, line_color='red')
    source_cum2 = ColumnDataSource(data={'x': [], 'y': []})
    p_cum.line('x', 'y', source=source_cum2, line_width=2, line_color='blue')

    # Create a button widget with a JavaScript callback
    plot_button = Button(label='Plot', button_type='success')

    # Define the CustomJS callback
    callback = CustomJS(args=dict(source=source, source2=source2,
        source_cum=source_cum, source_cum2=source_cum2,
        mu_input=mu_input, sigma_input=sigma_input,
        mu_input_2=mu_input_2, sigma_input_2=sigma_input_2), code="""
        var mu = parseFloat(mu_input.value);
        var sigma = parseFloat(sigma_input.value);
        var mu2 = parseFloat(mu_input_2.value);
        var sigma2 = parseFloat(sigma_input_2.value);
        if (!isNaN(mu) && !isNaN(sigma) && sigma > 0) {
            var x = [];
            var y = [];
            var y_cum = [];
            var x2 = [];
            var y2 = [];
            var y_cum_2 = [];

            // JavaScript doesn't have a built-in error function implementation
            // Using an approximation for erf function
            function erf(x) {
                // Constants for approximation
                var a1 =  0.254829592;
                var a2 = -0.284496736;
                var a3 =  1.421413741;
                var a4 = -1.453152027;
                var a5 =  1.061405429;
                var p  =  0.3275911;

                // Save the sign of x
                var sign = (x >= 0) ? 1 : -1;
                x = Math.abs(x);

                // Formula for approximation of erf
                var t = 1.0 / (1.0 + p * x);
                var y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-x * x);

                return sign * y;
            }

            for (var i = 0; i < 100; i++) {
                var x_val = mu - 4 * sigma + (8 * sigma * i / 99);
                x.push(x_val);

                var x_val_2 = mu2 - 4 * sigma2 + (8 * sigma2 * i / 99);
                x2.push(x_val_2);

                // PDF calculation
                y.push((1 / (sigma * Math.sqrt(2 * Math.PI))) * Math.exp(-0.5 * Math.pow((x_val - mu) / sigma, 2)));
                y2.push((1 / (sigma2 * Math.sqrt(2 * Math.PI))) * Math.exp(-0.5 * Math.pow((x_val_2 - mu2) / sigma2, 2)));

                // CDF calculation using the erf approximation
                y_cum.push(0.5 * (1 + erf((x_val - mu) / (sigma * Math.sqrt(2)))));
                y_cum_2.push(0.5 * (1 + erf((x_val_2 - mu2) / (sigma2 * Math.sqrt(2)))));
            }

            source.data = {x: x, y: y};
            source.change.emit();
            source_cum.data = {x: x, y: y_cum};
            source_cum.change.emit();
            source2.data = {x: x2, y: y2};
            source2.change.emit();
            source_cum2.data = {x: x2, y: y_cum_2};
            source_cum2.change.emit();
        }
    """)

    plot_button.js_on_event('button_click', callback)

    # Create the layout
    input_widgets = column(plain_text_div, mu_input, sigma_input,
                           plain_text_div_2, mu_input_2, sigma_input_2,
                           plot_button)
    plots = column(p, p_cum)
    layout = row(input_widgets, plots)

    return layout

# Enhanced version of create_gen_bokeh_plot
def create_gen_bokeh_plot():
    
    # Initialize notebook display for Bokeh
    # output_notebook()

    # Create distribution type selection widgets - now with Beta and Gumbel added
    dist_options = ["Normal", "LogNormal", "Exponential", "Beta", "Gumbel"]
    dist_type_1 = Select(title="Distribución 1:", value="Normal", options=dist_options, width=140)
    dist_type_2 = Select(title="Distribución 2:", value="Normal", options=dist_options, width=140)
    dist_type_3 = Select(title="Distribución 3:", value="Normal", options=dist_options, width=140)  # Added 3rd distribution

    # Create input widgets for distribution parameters
    
    # First distribution parameters
    box_width = 65
    param1_div_1 = Div(text="Mu:", width=box_width, height=10)
    param1_input_1 = TextInput(value='0', title="", width=box_width)
    param2_div_1 = Div(text="Sigma:", width=box_width, height=10)
    param2_input_1 = TextInput(value='1', title="", width=box_width)
    
    # Second distribution parameters
    param1_div_2 = Div(text="Mu:", width=box_width, height=10)
    param1_input_2 = TextInput(value='0', title="", width=box_width)
    param2_div_2 = Div(text="Sigma:", width=box_width, height=10)
    param2_input_2 = TextInput(value='1', title="", width=box_width)
    
    # Third distribution parameters (new)
    param1_div_3 = Div(text="Mu:", width=box_width, height=10)
    param1_input_3 = TextInput(value='0', title="", width=box_width)
    param2_div_3 = Div(text="Sigma:", width=box_width, height=10)
    param2_input_3 = TextInput(value='1', title="", width=box_width)

    # Create plots
    p = figure(title='Función de densidad', x_axis_label='x', y_axis_label='Density', height=300)
    source1 = ColumnDataSource(data={'x': [], 'y': []})
    p.line('x', 'y', source=source1, line_width=2, line_color='red')
    source2 = ColumnDataSource(data={'x': [], 'y': []})
    p.line('x', 'y', source=source2, line_width=2, line_color='blue')
    source3 = ColumnDataSource(data={'x': [], 'y': []})  # Added 3rd source
    p.line('x', 'y', source=source3, line_width=2, line_color='green')  # Added 3rd line

    p_cum = figure(title='Función de probabilidad acumulada', x_axis_label='x', y_axis_label='Cumulative', height=300)
    source_cum1 = ColumnDataSource(data={'x': [], 'y': []})
    p_cum.line('x', 'y', source=source_cum1, line_width=2, line_color='red')
    source_cum2 = ColumnDataSource(data={'x': [], 'y': []})
    p_cum.line('x', 'y', source=source_cum2, line_width=2, line_color='blue')
    source_cum3 = ColumnDataSource(data={'x': [], 'y': []})  # Added 3rd cumulative source
    p_cum.line('x', 'y', source=source_cum3, line_width=2, line_color='green')  # Added 3rd cumulative line

    # Create a button widget
    plot_button = Button(label='Plot', button_type='success')

    # JavaScript callback to update parameter labels based on distribution type
    update_params_callback = CustomJS(args=dict(
        dist_type_1=dist_type_1, 
        dist_type_2=dist_type_2,
        dist_type_3=dist_type_3,  # Added 3rd distribution type
        param1_div_1=param1_div_1,
        param2_div_1=param2_div_1,
        param1_div_2=param1_div_2,
        param2_div_2=param2_div_2,
        param1_div_3=param1_div_3,  # Added 3rd distribution parameter divs
        param2_div_3=param2_div_3,
        param1_input_1=param1_input_1,
        param2_input_1=param2_input_1,
        param1_input_2=param1_input_2,
        param2_input_2=param2_input_2,
        param1_input_3=param1_input_3,  # Added 3rd distribution parameter inputs
        param2_input_3=param2_input_3), code="""
        function updateLabels(distType, param1Div, param2Div, param2Input) {
            if (distType === "Normal") {
                param1Div.text = "Mu:";
                param2Div.text = "Sigma:";
                param2Input.visible = true;
            } else if (distType === "LogNormal") {
                param1Div.text = "LogMu:";
                param2Div.text = "LogSigma:";
                param2Input.visible = true;
            } else if (distType === "Exponential") {
                param1Div.text = "Rate (λ):";
                param2Div.text = "";
                param2Input.visible = false;
            } else if (distType === "Beta") {
                param1Div.text = "Alpha:";
                param2Div.text = "Beta:";
                param2Input.visible = true;
            } else if (distType === "Gumbel") {
                param1Div.text = "Location:";
                param2Div.text = "Scale:";
                param2Input.visible = true;
            }
        }
        
        // Update all three distributions
        updateLabels(dist_type_1.value, param1_div_1, param2_div_1, param2_input_1);
        updateLabels(dist_type_2.value, param1_div_2, param2_div_2, param2_input_2);
        updateLabels(dist_type_3.value, param1_div_3, param2_div_3, param2_input_3);
    """)

    # Attach callback to distribution type selectors
    dist_type_1.js_on_change('value', update_params_callback)
    dist_type_2.js_on_change('value', update_params_callback)
    dist_type_3.js_on_change('value', update_params_callback)  # Added callback for 3rd distribution

    # Define the plotting CustomJS callback
    plot_callback = CustomJS(args=dict(
        source1=source1, source2=source2, source3=source3,  # Added 3rd source
        source_cum1=source_cum1, source_cum2=source_cum2, source_cum3=source_cum3,  # Added 3rd cumulative source
        param1_input_1=param1_input_1, param2_input_1=param2_input_1,
        param1_input_2=param1_input_2, param2_input_2=param2_input_2,
        param1_input_3=param1_input_3, param2_input_3=param2_input_3,  # Added 3rd inputs
        dist_type_1=dist_type_1, dist_type_2=dist_type_2, dist_type_3=dist_type_3), code="""
        // Parse all parameter values
        var param1_1 = parseFloat(param1_input_1.value);
        var param2_1 = parseFloat(param2_input_1.value);
        var param1_2 = parseFloat(param1_input_2.value);
        var param2_2 = parseFloat(param2_input_2.value);
        var param1_3 = parseFloat(param1_input_3.value);
        var param2_3 = parseFloat(param2_input_3.value);
        var dist1 = dist_type_1.value;
        var dist2 = dist_type_2.value;
        var dist3 = dist_type_3.value;
        
        // Validate parameters
        function validateParams(dist, param1, param2) {
            if (isNaN(param1)) return false;
            
            if (dist === "Normal" || dist === "LogNormal" || dist === "Gumbel") {
                if (isNaN(param2) || param2 <= 0) return false;
            } else if (dist === "Exponential") {
                if (param1 <= 0) return false;
            } else if (dist === "Beta") {
                if (isNaN(param2) || param1 <= 0 || param2 <= 0) return false;
            }
            
            return true;
        }
        
        var is_valid = validateParams(dist1, param1_1, param2_1) && 
                       validateParams(dist2, param1_2, param2_2) &&
                       validateParams(dist3, param1_3, param2_3);
        
        if (is_valid) {
            // JavaScript doesn't have a built-in error function implementation
            // Using an approximation for erf function
            function erf(x) {
                // Constants for approximation
                var a1 =  0.254829592;
                var a2 = -0.284496736;
                var a3 =  1.421413741;
                var a4 = -1.453152027;
                var a5 =  1.061405429;
                var p  =  0.3275911;

                // Save the sign of x
                var sign = (x >= 0) ? 1 : -1;
                x = Math.abs(x);

                // Formula for approximation of erf
                var t = 1.0 / (1.0 + p * x);
                var y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-x * x);

                return sign * y;
            }
            
            // Functions for different distributions
            function normalPDF(x, mean, stdDev) {
                return (1 / (stdDev * Math.sqrt(2 * Math.PI))) * 
                       Math.exp(-0.5 * Math.pow((x - mean) / stdDev, 2));
            }
            
            function normalCDF(x, mean, stdDev) {
                return 0.5 * (1 + erf((x - mean) / (stdDev * Math.sqrt(2))));
            }
            
            function lognormalPDF(x, logmu, logsigma) {
                if (x <= 0) return 0;
                return (1 / (x * logsigma * Math.sqrt(2 * Math.PI))) * 
                       Math.exp(-0.5 * Math.pow((Math.log(x) - logmu) / logsigma, 2));
            }
            
            function lognormalCDF(x, logmu, logsigma) {
                if (x <= 0) return 0;
                return 0.5 * (1 + erf((Math.log(x) - logmu) / (logsigma * Math.sqrt(2))));
            }
            
            function exponentialPDF(x, rate) {
                if (x < 0) return 0;
                return rate * Math.exp(-rate * x);
            }
            
            function exponentialCDF(x, rate) {
                if (x < 0) return 0;
                return 1 - Math.exp(-rate * x);
            }
            
            // Beta distribution functions
            function betaPDF(x, alpha, beta) {
                if (x < 0 || x > 1) return 0;
                
                // Simple approximation for Beta function B(alpha, beta)
                function logBeta(a, b) {
                    return Math.log(Math.exp(a) * Math.exp(b) / Math.exp(a + b));
                }
                
                if (x === 0) {
                    return alpha > 1 ? 0 : alpha === 1 ? 1 : Infinity;
                }
                if (x === 1) {
                    return beta > 1 ? 0 : beta === 1 ? 1 : Infinity;
                }
                
                // Use logarithms to avoid numerical issues
                var logBetaAB = logBeta(alpha, beta);
                var logPDF = (alpha - 1) * Math.log(x) + (beta - 1) * Math.log(1 - x) - logBetaAB;
                return Math.exp(logPDF);
            }
            
            function betaCDF(x, alpha, beta) {
                // Simple approximation for beta CDF
                if (x <= 0) return 0;
                if (x >= 1) return 1;
                
                // Approximation using normal distribution when alpha and beta are large enough
                if (alpha > 5 && beta > 5) {
                    var mu = alpha / (alpha + beta);
                    var variance = (alpha * beta) / (Math.pow(alpha + beta, 2) * (alpha + beta + 1));
                    var sigma = Math.sqrt(variance);
                    return normalCDF(x, mu, sigma);
                }
                
                // For smaller alpha/beta, use a very rough approximation
                // (this is not accurate but gives a sense of the shape)
                if (x < 0.5) {
                    return Math.pow(x, alpha) / alpha;
                } else {
                    return 1 - Math.pow(1 - x, beta) / beta;
                }
            }
            
            // Gumbel distribution functions
            function gumbelPDF(x, location, scale) {
                var z = (x - location) / scale;
                return (1 / scale) * Math.exp(-(z + Math.exp(-z)));
            }
            
            function gumbelCDF(x, location, scale) {
                var z = (x - location) / scale;
                return Math.exp(-Math.exp(-z));
            }
            
            // Calculate ranges for each distribution
            function calculateRange(dist, param1, param2) {
                var min, max;
                
                if (dist === "Normal") {
                    min = param1 - 4 * param2;
                    max = param1 + 4 * param2;
                } else if (dist === "LogNormal") {
                    min = Math.max(0.01, Math.exp(param1 - 4 * param2));
                    max = Math.exp(param1 + 4 * param2);
                } else if (dist === "Exponential") {
                    min = 0;
                    max = 5 / param1; // Using 5/lambda as a reasonable upper bound
                } else if (dist === "Beta") {
                    min = 0;
                    max = 1;
                } else if (dist === "Gumbel") {
                    min = param1 - 4 * param2;
                    max = param1 + 6 * param2; // Gumbel is right-skewed
                }
                
                return {min: min, max: max};
            }
            
            var range1 = calculateRange(dist1, param1_1, param2_1);
            var range2 = calculateRange(dist2, param1_2, param2_2);
            var range3 = calculateRange(dist3, param1_3, param2_3);
            
            // Calculate the points for each distribution
            function calculatePoints(dist, param1, param2, range) {
                var x = [];
                var y_pdf = [];
                var y_cdf = [];
                
                for (var i = 0; i < 100; i++) {
                    var x_val = range.min + (range.max - range.min) * i / 99;
                    x.push(x_val);
                    
                    if (dist === "Normal") {
                        y_pdf.push(normalPDF(x_val, param1, param2));
                        y_cdf.push(normalCDF(x_val, param1, param2));
                    } else if (dist === "LogNormal") {
                        y_pdf.push(lognormalPDF(x_val, param1, param2));
                        y_cdf.push(lognormalCDF(x_val, param1, param2));
                    } else if (dist === "Exponential") {
                        y_pdf.push(exponentialPDF(x_val, param1));
                        y_cdf.push(exponentialCDF(x_val, param1));
                    } else if (dist === "Beta") {
                        y_pdf.push(betaPDF(x_val, param1, param2));
                        y_cdf.push(betaCDF(x_val, param1, param2));
                    } else if (dist === "Gumbel") {
                        y_pdf.push(gumbelPDF(x_val, param1, param2));
                        y_cdf.push(gumbelCDF(x_val, param1, param2));
                    }
                }
                
                return {x: x, y_pdf: y_pdf, y_cdf: y_cdf};
            }
            
            var points1 = calculatePoints(dist1, param1_1, param2_1, range1);
            var points2 = calculatePoints(dist2, param1_2, param2_2, range2);
            var points3 = calculatePoints(dist3, param1_3, param2_3, range3);
            
            // Update the data sources
            source1.data = {x: points1.x, y: points1.y_pdf};
            source1.change.emit();
            source_cum1.data = {x: points1.x, y: points1.y_cdf};
            source_cum1.change.emit();
            
            source2.data = {x: points2.x, y: points2.y_pdf};
            source2.change.emit();
            source_cum2.data = {x: points2.x, y: points2.y_cdf};
            source_cum2.change.emit();
            
            source3.data = {x: points3.x, y: points3.y_pdf};
            source3.change.emit();
            source_cum3.data = {x: points3.x, y: points3.y_cdf};
            source_cum3.change.emit();
        }
    """)

    plot_button.js_on_event('button_click', plot_callback)

    # Create layout with side-by-side parameter inputs
    dist1_params = row(
        column(param1_div_1, param1_input_1),
        column(param2_div_1, param2_input_1)
    )
    dist2_params = row(
        column(param1_div_2, param1_input_2),
        column(param2_div_2, param2_input_2)
    )
    dist3_params = row(
        column(param1_div_3, param1_input_3),
        column(param2_div_3, param2_input_3)
    )

    input_widgets = column(
        dist_type_1,
        dist1_params,
        dist_type_2,
        dist2_params,
        dist_type_3,
        dist3_params,
        plot_button
    )
    
    plots = column(p, p_cum)
    layout = row(input_widgets, plots)

    return layout