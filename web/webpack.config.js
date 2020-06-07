const path = require('path');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
        entry: './src/index.js',
        watchOptions: {
                aggregateTimeout: 250,
                ignored: /node_modules/,
                poll: 100
        },
        plugins: [
                new CleanWebpackPlugin(),
                new HtmlWebpackPlugin({
                        title: 'Caching',
                }),
        ],
        module: {
                rules: [
                        {
                                test: /\.css$/i,
                                use: ['style-loader', 'css-loader'],
                        },
                ],
        },
        output: {
                filename: '[name].[contenthash].js',
                path: path.resolve(__dirname, 'bin'),
        },
        optimization: {
                moduleIds: 'hashed',
                runtimeChunk: 'single',
                splitChunks: {
                        cacheGroups: {
                                vendor: {
                                        test: /[\\/]node_modules[\\/]/,
                                        name: 'vendors',
                                        chunks: 'all',
                                },
                        },
                },
        },
};
