from tensorflow.keras import layers, models
import tensorflow as tf

def make_generator_model(num_classes, noise_dim):
    # Noise input
    noise = layers.Input(shape=(noise_dim,))
    # Conditional label
    label = layers.Input(shape=(1,), dtype='int32')
    # Embedding for categorical input
    label_embedding = layers.Embedding(num_classes, noise_dim)(label)
    # Flatten the embedding
    label_embedding = layers.Flatten()(label_embedding)
    # Element-wise product of the noise and label
    model_input = layers.multiply([noise, label_embedding])

    x = layers.Dense(128, use_bias=False)(model_input)
    x = layers.BatchNormalization()(x)
    x = layers.LeakyReLU()(x)

    x = layers.Dense(256, use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    x = layers.LeakyReLU()(x)

    x = layers.Dense(512, use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    x = layers.LeakyReLU()(x)

    x = layers.Dense(28*28*1, activation='tanh', use_bias=False)(x)
    output = layers.Reshape((28, 28, 1))(x)

    return models.Model([noise, label], output)

def make_discriminator_model(num_classes, input_shape):
    # Image input
    image = layers.Input(shape=input_shape)
    # Conditional label
    label = layers.Input(shape=(1,), dtype='int32')
    # Embedding for categorical input
    label_embedding = layers.Embedding(num_classes, input_shape[0] * input_shape[1] * input_shape[2])(label)
    # Reshape and scale label embedding to match image shape
    label_embedding = layers.Flatten()(label_embedding)
    label_embedding = layers.Reshape(input_shape)(label_embedding)

    # Concatenate image and label
    concatenated = layers.Concatenate(axis=-1)([image, label_embedding])

    x = layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=input_shape)(concatenated)
    x = layers.LeakyReLU()(x)
    x = layers.Dropout(0.3)(x)

    x = layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same')(x)
    x = layers.LeakyReLU()(x)
    x = layers.Dropout(0.3)(x)

    x = layers.Flatten()(x)
    x = layers.Dense(1)(x)

    return models.Model([image, label], x)

cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)

def discriminator_loss(real_output, fake_output):
    real_loss = cross_entropy(tf.ones_like(real_output), real_output)
    fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)
    total_loss = real_loss + fake_loss
    return total_loss

def generator_loss(fake_output):
    return cross_entropy(tf.ones_like(fake_output), fake_output)
