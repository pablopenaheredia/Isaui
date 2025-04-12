namespace ProyectoIsaui
{
    partial class FrmProducto
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.GbProducto = new System.Windows.Forms.GroupBox();
            this.txtstock = new System.Windows.Forms.TextBox();
            this.lblMarca = new System.Windows.Forms.Label();
            this.txtcodbarra = new System.Windows.Forms.TextBox();
            this.lblstock = new System.Windows.Forms.Label();
            this.txtCodProducto = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.txtprecio = new System.Windows.Forms.TextBox();
            this.btncancelar = new System.Windows.Forms.Button();
            this.btnguardar = new System.Windows.Forms.Button();
            this.txtmarca = new System.Windows.Forms.TextBox();
            this.lblprecio = new System.Windows.Forms.Label();
            this.txtNombre = new System.Windows.Forms.TextBox();
            this.LblNombre = new System.Windows.Forms.Label();
            this.GbProducto.SuspendLayout();
            this.SuspendLayout();
            // 
            // GbProducto
            // 
            this.GbProducto.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.GbProducto.Controls.Add(this.txtstock);
            this.GbProducto.Controls.Add(this.lblMarca);
            this.GbProducto.Controls.Add(this.txtcodbarra);
            this.GbProducto.Controls.Add(this.lblstock);
            this.GbProducto.Controls.Add(this.txtCodProducto);
            this.GbProducto.Controls.Add(this.label1);
            this.GbProducto.Controls.Add(this.txtprecio);
            this.GbProducto.Controls.Add(this.btncancelar);
            this.GbProducto.Controls.Add(this.btnguardar);
            this.GbProducto.Controls.Add(this.txtmarca);
            this.GbProducto.Controls.Add(this.lblprecio);
            this.GbProducto.Controls.Add(this.txtNombre);
            this.GbProducto.Controls.Add(this.LblNombre);
            this.GbProducto.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.GbProducto.Location = new System.Drawing.Point(35, 11);
            this.GbProducto.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.GbProducto.Name = "GbProducto";
            this.GbProducto.Padding = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.GbProducto.Size = new System.Drawing.Size(653, 317);
            this.GbProducto.TabIndex = 0;
            this.GbProducto.TabStop = false;
            this.GbProducto.Text = "Informacion del producto";
            this.GbProducto.Enter += new System.EventHandler(this.GbProducto_Enter);
            // 
            // txtstock
            // 
            this.txtstock.Location = new System.Drawing.Point(166, 198);
            this.txtstock.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtstock.Name = "txtstock";
            this.txtstock.Size = new System.Drawing.Size(389, 22);
            this.txtstock.TabIndex = 11;
            // 
            // lblMarca
            // 
            this.lblMarca.AutoSize = true;
            this.lblMarca.Location = new System.Drawing.Point(34, 76);
            this.lblMarca.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblMarca.Name = "lblMarca";
            this.lblMarca.Size = new System.Drawing.Size(45, 16);
            this.lblMarca.TabIndex = 10;
            this.lblMarca.Text = "Marca";
            // 
            // txtcodbarra
            // 
            this.txtcodbarra.Location = new System.Drawing.Point(166, 161);
            this.txtcodbarra.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtcodbarra.Name = "txtcodbarra";
            this.txtcodbarra.Size = new System.Drawing.Size(389, 22);
            this.txtcodbarra.TabIndex = 9;
            // 
            // lblstock
            // 
            this.lblstock.AutoSize = true;
            this.lblstock.Location = new System.Drawing.Point(34, 198);
            this.lblstock.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblstock.Name = "lblstock";
            this.lblstock.Size = new System.Drawing.Size(41, 16);
            this.lblstock.TabIndex = 8;
            this.lblstock.Text = "Stock";
            // 
            // txtCodProducto
            // 
            this.txtCodProducto.Location = new System.Drawing.Point(516, 293);
            this.txtCodProducto.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtCodProducto.Name = "txtCodProducto";
            this.txtCodProducto.Size = new System.Drawing.Size(116, 22);
            this.txtCodProducto.TabIndex = 7;
            this.txtCodProducto.Visible = false;
            this.txtCodProducto.TextChanged += new System.EventHandler(this.txtCodProducto_TextChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(34, 161);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(106, 16);
            this.label1.TabIndex = 6;
            this.label1.Text = "Codigo de Barra";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // txtprecio
            // 
            this.txtprecio.Location = new System.Drawing.Point(166, 119);
            this.txtprecio.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtprecio.Name = "txtprecio";
            this.txtprecio.Size = new System.Drawing.Size(389, 22);
            this.txtprecio.TabIndex = 4;
            // 
            // btncancelar
            // 
            this.btncancelar.Location = new System.Drawing.Point(386, 249);
            this.btncancelar.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.btncancelar.Name = "btncancelar";
            this.btncancelar.Size = new System.Drawing.Size(149, 47);
            this.btncancelar.TabIndex = 5;
            this.btncancelar.Text = "Cancelar";
            this.btncancelar.UseVisualStyleBackColor = true;
            this.btncancelar.Click += new System.EventHandler(this.btncancelar_Click);
            // 
            // btnguardar
            // 
            this.btnguardar.Location = new System.Drawing.Point(166, 249);
            this.btnguardar.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.btnguardar.Name = "btnguardar";
            this.btnguardar.Size = new System.Drawing.Size(149, 47);
            this.btnguardar.TabIndex = 4;
            this.btnguardar.Text = "Guardar";
            this.btnguardar.UseVisualStyleBackColor = true;
            this.btnguardar.Click += new System.EventHandler(this.btnguardar_Click);
            // 
            // txtmarca
            // 
            this.txtmarca.Location = new System.Drawing.Point(166, 76);
            this.txtmarca.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtmarca.Name = "txtmarca";
            this.txtmarca.Size = new System.Drawing.Size(389, 22);
            this.txtmarca.TabIndex = 3;
            this.txtmarca.TextChanged += new System.EventHandler(this.txtmarca_TextChanged);
            // 
            // lblprecio
            // 
            this.lblprecio.AutoSize = true;
            this.lblprecio.Location = new System.Drawing.Point(34, 119);
            this.lblprecio.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblprecio.Name = "lblprecio";
            this.lblprecio.Size = new System.Drawing.Size(46, 16);
            this.lblprecio.TabIndex = 2;
            this.lblprecio.Text = "Precio";
            // 
            // txtNombre
            // 
            this.txtNombre.Location = new System.Drawing.Point(166, 35);
            this.txtNombre.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.txtNombre.Name = "txtNombre";
            this.txtNombre.Size = new System.Drawing.Size(389, 22);
            this.txtNombre.TabIndex = 1;
            // 
            // LblNombre
            // 
            this.LblNombre.AutoSize = true;
            this.LblNombre.Location = new System.Drawing.Point(34, 35);
            this.LblNombre.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.LblNombre.Name = "LblNombre";
            this.LblNombre.Size = new System.Drawing.Size(56, 16);
            this.LblNombre.TabIndex = 0;
            this.LblNombre.Text = "Nombre";
            // 
            // FrmProducto
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.ClientSize = new System.Drawing.Size(724, 350);
            this.Controls.Add(this.GbProducto);
            this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.Name = "FrmProducto";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Show;
            this.Text = "Formulario de Producto";
            this.Load += new System.EventHandler(this.FrmProducto_Load);
            this.GbProducto.ResumeLayout(false);
            this.GbProducto.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox GbProducto;
        private System.Windows.Forms.Button btnguardar;
        private System.Windows.Forms.TextBox txtmarca;
        private System.Windows.Forms.Label lblprecio;
        private System.Windows.Forms.TextBox txtNombre;
        private System.Windows.Forms.Label LblNombre;
        private System.Windows.Forms.Button btncancelar;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtprecio;
        private System.Windows.Forms.TextBox txtCodProducto;
        private System.Windows.Forms.TextBox txtcodbarra;
        private System.Windows.Forms.Label lblstock;
        private System.Windows.Forms.TextBox txtstock;
        private System.Windows.Forms.Label lblMarca;
    }
}