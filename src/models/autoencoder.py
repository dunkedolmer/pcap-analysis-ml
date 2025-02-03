import torch.nn as nn

class Autoencoder(nn.Module):
    def __init__(self, input_dim=256, latent_dim=32):
        super(Autoencoder, self).__init__()
        
        # ======= ENCODER (Compression) =======
        self.encoder = nn.Sequential(
            # First layer: Compress input from original (full size) to 128 neurons
            nn.Linear(input_dim, 128),
            nn.ReLU(), # Activation to introduce non-linearity
            
            # Second layer: Further compression to 64 neurons
            nn.Linear(128, 64),
            nn.ReLU(),
            
            # Third layer: Reducing data to the latent space (smallest representation)
            nn.Linear(64, latent_dim) # The bottleneck layer (most compressed form)
        )

        # ======= DECODER (Reconstruction) =======
        self.decoder = nn.Sequential(
            # First layer: Expand from the latent space back to 64 neurons
            nn.Linear(latent_dim, 64),
            nn.ReLU(),

            # Second layer: Further expansion to 128 neurons
            nn.Linear(64, 128),
            nn.ReLU(),

            # Output layer: Expanding back to the original input size
            nn.Linear(128, input_dim),

            # Sigmoid activation ensures output values remain between 0 and 1
            nn.Sigmoid()
        ) 
    
    def forward(self, x):
        # (x, g(f(x)))
        encoded = self.encoder(x) # f(x)
        decoded = self.decoder(encoded) # g(x)
        return decoded
    